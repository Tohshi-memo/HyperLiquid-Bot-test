# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T22:52:35.173538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.0712` n `234`; crypto_major avg `-0.0222` n `8`; equity avg `-0.0298` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0025` n `20`; unknown avg `5.8331` n `942`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.1033` n `234`; crypto_major avg `-0.023` n `8`; equity avg `-0.0746` n `140`; fx avg `-0.0145` n `6`; index avg `-0.023` n `26`; metal avg `-0.0013` n `20`; unknown avg `16.4744` n `930`
- 4h: commodity avg `-0.001` n `12`; crypto_alt avg `0.8864` n `234`; crypto_major avg `0.4608` n `8`; equity avg `0.4716` n `140`; fx avg `0.032` n `6`; index avg `0.0708` n `26`; metal avg `-0.0381` n `20`; unknown avg `0.5293` n `872`
- 24h: commodity avg `-0.0813` n `12`; crypto_alt avg `6.8988` n `234`; crypto_major avg `6.9304` n `8`; equity avg `1.3386` n `140`; fx avg `0.2348` n `6`; index avg `0.0532` n `26`; metal avg `0.3783` n `20`; unknown avg `4.0793` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
