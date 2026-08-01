# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T12:37:29.608656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `-0.0302` n `230`; crypto_major avg `-0.0365` n `8`; equity avg `-0.0282` n `102`; fx avg `-0.0032` n `6`; index avg `0.0122` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0357` n `782`
- 1h: commodity avg `0.0385` n `12`; crypto_alt avg `0.1832` n `230`; crypto_major avg `0.0429` n `8`; equity avg `-0.0831` n `102`; fx avg `0.0501` n `6`; index avg `0.0053` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0404` n `781`
- 4h: commodity avg `0.0744` n `12`; crypto_alt avg `-0.0394` n `230`; crypto_major avg `-0.1776` n `8`; equity avg `-0.1069` n `102`; fx avg `-0.0957` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0926` n `781`
- 24h: commodity avg `0.4413` n `12`; crypto_alt avg `0.5411` n `230`; crypto_major avg `-1.1742` n `8`; equity avg `-2.1425` n `102`; fx avg `-0.1599` n `6`; index avg `-0.2022` n `25`; metal avg `-0.0075` n `20`; unknown avg `4.4754` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
