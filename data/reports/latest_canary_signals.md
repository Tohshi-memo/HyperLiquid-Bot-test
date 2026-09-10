# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T18:52:31.243999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0883` n `12`; crypto_alt avg `0.3005` n `233`; crypto_major avg `0.2425` n `8`; equity avg `0.0848` n `135`; fx avg `0.0018` n `6`; index avg `0.0325` n `26`; metal avg `0.0635` n `20`; unknown avg `0.0329` n `797`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.1746` n `233`; crypto_major avg `-0.2387` n `8`; equity avg `-0.1404` n `135`; fx avg `-0.0049` n `6`; index avg `0.0099` n `26`; metal avg `-0.0816` n `20`; unknown avg `0.3106` n `795`
- 4h: commodity avg `0.3851` n `12`; crypto_alt avg `0.1412` n `233`; crypto_major avg `-0.017` n `8`; equity avg `-0.5895` n `135`; fx avg `0.0081` n `6`; index avg `-0.0665` n `26`; metal avg `-0.2024` n `20`; unknown avg `0.2739` n `788`
- 24h: commodity avg `0.8527` n `12`; crypto_alt avg `-4.0899` n `233`; crypto_major avg `-3.3049` n `8`; equity avg `-1.9833` n `135`; fx avg `0.0872` n `6`; index avg `-0.3086` n `26`; metal avg `-1.2233` n `20`; unknown avg `0.0656` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
