# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T21:37:33.213892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `0.253` n `238`; crypto_major avg `0.2333` n `8`; equity avg `0.0604` n `156`; fx avg `-0.0104` n `6`; index avg `0.0102` n `27`; metal avg `0.0017` n `20`; unknown avg `0.3782` n `1263`
- 1h: commodity avg `0.0165` n `13`; crypto_alt avg `0.2014` n `238`; crypto_major avg `0.2203` n `8`; equity avg `0.1307` n `156`; fx avg `-0.0285` n `6`; index avg `0.0347` n `27`; metal avg `-0.0009` n `20`; unknown avg `1.7736` n `1249`
- 4h: commodity avg `0.0374` n `13`; crypto_alt avg `-0.544` n `238`; crypto_major avg `-0.2663` n `8`; equity avg `-0.0922` n `156`; fx avg `-0.0372` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0216` n `20`; unknown avg `166.8569` n `1207`
- 24h: commodity avg `0.0334` n `13`; crypto_alt avg `-0.4796` n `238`; crypto_major avg `0.0533` n `8`; equity avg `0.3683` n `156`; fx avg `-0.0371` n `6`; index avg `0.0863` n `27`; metal avg `0.0395` n `20`; unknown avg `4.2496` n `1016`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
