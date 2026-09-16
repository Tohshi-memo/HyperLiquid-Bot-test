# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T11:07:31.351593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.0554` n `234`; crypto_major avg `0.1365` n `8`; equity avg `0.094` n `137`; fx avg `-0.0036` n `6`; index avg `0.0141` n `27`; metal avg `0.0395` n `20`; unknown avg `0.14` n `917`
- 1h: commodity avg `-0.0356` n `10`; crypto_alt avg `0.1216` n `232`; crypto_major avg `0.1675` n `7`; equity avg `0.1623` n `132`; fx avg `-0.0023` n `6`; index avg `0.0283` n `23`; metal avg `0.1682` n `13`; unknown avg `0.2099` n `898`
- 4h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.2536` n `234`; crypto_major avg `-0.0842` n `8`; equity avg `0.0457` n `137`; fx avg `0.0014` n `6`; index avg `0.0247` n `27`; metal avg `0.0222` n `20`; unknown avg `-0.2454` n `911`
- 24h: commodity avg `0.2201` n `12`; crypto_alt avg `-2.8312` n `234`; crypto_major avg `-2.7452` n `8`; equity avg `-0.2629` n `137`; fx avg `0.1222` n `6`; index avg `0.0713` n `27`; metal avg `0.5253` n `20`; unknown avg `18889.387` n `798`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
