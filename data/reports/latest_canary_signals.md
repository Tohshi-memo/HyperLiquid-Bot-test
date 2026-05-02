# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T14:39:07.801693+00:00`
- Correlation status: `ready`
- Asset price records: `81`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `7`; crypto_alt avg `0.1204` n `223`; crypto_major avg `0.0757` n `7`; equity avg `-0.055` n `42`; fx avg `0.0037` n `4`; index avg `-0.0057` n `9`; metal avg `-0.0044` n `7`; unknown avg `0.2614` n `313`
- 1h: commodity avg `0.0038` n `7`; crypto_alt avg `0.5197` n `223`; crypto_major avg `0.0638` n `7`; equity avg `-0.0568` n `42`; fx avg `0.0099` n `4`; index avg `-0.0131` n `9`; metal avg `-0.0247` n `7`; unknown avg `0.1581` n `313`
- 4h: commodity avg `-0.0344` n `7`; crypto_alt avg `0.7118` n `223`; crypto_major avg `0.1728` n `7`; equity avg `-0.0436` n `42`; fx avg `-0.0133` n `4`; index avg `0.0432` n `9`; metal avg `-0.0167` n `7`; unknown avg `0.1101` n `313`
- 24h: commodity avg `0.6189` n `7`; crypto_alt avg `0.8023` n `223`; crypto_major avg `0.0919` n `7`; equity avg `0.7683` n `42`; fx avg `-0.1374` n `4`; index avg `0.0231` n `9`; metal avg `-0.7359` n `7`; unknown avg `1.4053` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.538`, n `77`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5194`, n `77`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5177`, n `73`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5088`, n `73`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4769`, n `73`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4651`, n `73`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4648`, n `73`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4637`, n `77`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4423`, n `77`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4247`, n `73`, moderate_sample_signal
