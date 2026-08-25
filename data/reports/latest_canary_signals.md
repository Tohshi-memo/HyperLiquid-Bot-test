# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T08:56:06.700109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1053` n `12`; crypto_alt avg `-0.4069` n `231`; crypto_major avg `-0.4722` n `8`; equity avg `-0.0237` n `122`; fx avg `0.014` n `6`; index avg `0.0081` n `25`; metal avg `-0.0598` n `20`; unknown avg `-0.1103` n `794`
- 1h: commodity avg `-0.278` n `12`; crypto_alt avg `0.1313` n `231`; crypto_major avg `-0.0899` n `8`; equity avg `0.2134` n `122`; fx avg `0.0055` n `6`; index avg `0.0443` n `25`; metal avg `-0.099` n `20`; unknown avg `-0.0732` n `794`
- 4h: commodity avg `-0.3667` n `12`; crypto_alt avg `-1.0405` n `231`; crypto_major avg `-0.85` n `8`; equity avg `0.5169` n `122`; fx avg `0.0683` n `6`; index avg `0.1064` n `25`; metal avg `-0.0407` n `20`; unknown avg `-0.3246` n `778`
- 24h: commodity avg `-0.4155` n `12`; crypto_alt avg `1.129` n `231`; crypto_major avg `2.247` n `8`; equity avg `0.2309` n `122`; fx avg `0.0423` n `6`; index avg `0.0413` n `25`; metal avg `-0.2515` n `20`; unknown avg `0.1718` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
