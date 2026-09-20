# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T01:35:11.170164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.4047` n `234`; crypto_major avg `-0.2989` n `8`; equity avg `-0.0061` n `140`; fx avg `-0.0121` n `6`; index avg `-0.0012` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.0758` n `943`
- 1h: commodity avg `0.0521` n `12`; crypto_alt avg `-0.7151` n `234`; crypto_major avg `-0.4889` n `8`; equity avg `-0.0009` n `140`; fx avg `0.0023` n `6`; index avg `0.0088` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.014` n `941`
- 4h: commodity avg `0.1099` n `12`; crypto_alt avg `0.6294` n `234`; crypto_major avg `-0.0573` n `8`; equity avg `0.0438` n `140`; fx avg `-0.0017` n `6`; index avg `-0.0214` n `26`; metal avg `0.011` n `20`; unknown avg `0.3388` n `911`
- 24h: commodity avg `0.0408` n `12`; crypto_alt avg `1.1472` n `234`; crypto_major avg `-0.53` n `8`; equity avg `0.114` n `140`; fx avg `-0.0705` n `6`; index avg `0.0103` n `26`; metal avg `0.0355` n `20`; unknown avg `0.3738` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
