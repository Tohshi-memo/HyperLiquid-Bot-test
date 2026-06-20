# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T22:54:46.664390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0964` n `228`; crypto_major avg `-0.0325` n `8`; equity avg `0.0109` n `78`; fx avg `-0.0013` n `6`; index avg `0.004` n `23`; metal avg `-0.0161` n `18`; unknown avg `1.2388` n `701`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.591` n `228`; crypto_major avg `0.5771` n `8`; equity avg `0.1037` n `78`; fx avg `0.0104` n `6`; index avg `0.0367` n `23`; metal avg `0.0242` n `18`; unknown avg `0.8193` n `701`
- 4h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.7082` n `228`; crypto_major avg `0.9687` n `8`; equity avg `0.3025` n `78`; fx avg `0.0017` n `6`; index avg `0.0455` n `23`; metal avg `0.0152` n `18`; unknown avg `0.0806` n `701`
- 24h: commodity avg `0.1717` n `12`; crypto_alt avg `1.3504` n `228`; crypto_major avg `1.7969` n `8`; equity avg `0.5257` n `78`; fx avg `0.0633` n `6`; index avg `0.1043` n `23`; metal avg `-0.0715` n `18`; unknown avg `-0.3189` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
