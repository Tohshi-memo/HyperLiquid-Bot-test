# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T03:52:30.398417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.4958` n `235`; crypto_major avg `-0.3251` n `8`; equity avg `-0.0243` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0011` n `20`; unknown avg `1.1382` n `1117`
- 1h: commodity avg `0.0807` n `13`; crypto_alt avg `-1.2168` n `235`; crypto_major avg `-0.5692` n `8`; equity avg `-0.1229` n `150`; fx avg `-0.0013` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.836` n `1115`
- 4h: commodity avg `0.0997` n `13`; crypto_alt avg `-1.0965` n `235`; crypto_major avg `-0.587` n `8`; equity avg `-0.1253` n `150`; fx avg `0.0023` n `6`; index avg `-0.0208` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.1011` n `1109`
- 24h: commodity avg `0.1855` n `13`; crypto_alt avg `0.1957` n `235`; crypto_major avg `-0.0797` n `8`; equity avg `-0.0399` n `150`; fx avg `-0.0058` n `6`; index avg `-0.0321` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.1722` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
