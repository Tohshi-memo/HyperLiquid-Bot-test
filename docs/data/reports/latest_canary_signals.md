# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T00:37:25.329067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `13`; crypto_alt avg `0.0115` n `235`; crypto_major avg `0.0072` n `8`; equity avg `0.0116` n `150`; fx avg `0.0011` n `6`; index avg `0.0095` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0148` n `1116`
- 1h: commodity avg `0.01` n `13`; crypto_alt avg `0.4905` n `235`; crypto_major avg `0.1856` n `8`; equity avg `0.0639` n `150`; fx avg `0.0044` n `6`; index avg `0.0236` n `26`; metal avg `0.0302` n `20`; unknown avg `-0.0081` n `1108`
- 4h: commodity avg `-0.0506` n `13`; crypto_alt avg `1.7035` n `235`; crypto_major avg `0.6561` n `8`; equity avg `0.0778` n `150`; fx avg `0.0039` n `6`; index avg `0.0309` n `26`; metal avg `0.0019` n `20`; unknown avg `0.3238` n `1092`
- 24h: commodity avg `-0.1693` n `13`; crypto_alt avg `2.9595` n `235`; crypto_major avg `0.68` n `8`; equity avg `0.7682` n `150`; fx avg `-0.0305` n `6`; index avg `0.1113` n `26`; metal avg `0.4501` n `20`; unknown avg `13.0667` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
