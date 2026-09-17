# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T05:52:31.896702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0573` n `12`; crypto_alt avg `0.0493` n `234`; crypto_major avg `0.0997` n `8`; equity avg `-0.0113` n `137`; fx avg `-0.0272` n `6`; index avg `-0.003` n `27`; metal avg `0.0191` n `20`; unknown avg `0.5957` n `921`
- 1h: commodity avg `-0.0907` n `12`; crypto_alt avg `0.0273` n `234`; crypto_major avg `-0.1132` n `8`; equity avg `-0.2557` n `137`; fx avg `-0.0079` n `6`; index avg `-0.0779` n `27`; metal avg `-0.0204` n `20`; unknown avg `9.1748` n `919`
- 4h: commodity avg `-0.0842` n `12`; crypto_alt avg `0.4595` n `234`; crypto_major avg `-0.1107` n `8`; equity avg `0.0081` n `137`; fx avg `-0.025` n `6`; index avg `-0.0447` n `27`; metal avg `0.0239` n `20`; unknown avg `0.7667` n `911`
- 24h: commodity avg `-0.5221` n `12`; crypto_alt avg `2.4787` n `234`; crypto_major avg `1.2824` n `8`; equity avg `0.8574` n `137`; fx avg `-0.0051` n `6`; index avg `0.0333` n `27`; metal avg `-0.2327` n `20`; unknown avg `0.2945` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
