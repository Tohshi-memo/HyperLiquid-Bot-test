# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T06:37:28.542994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.0497` n `228`; crypto_major avg `-0.0384` n `8`; equity avg `0.0884` n `79`; fx avg `0.04` n `6`; index avg `0.0152` n `23`; metal avg `0.0267` n `18`; unknown avg `-0.0441` n `701`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0275` n `228`; crypto_major avg `-0.1566` n `8`; equity avg `0.2017` n `79`; fx avg `0.0287` n `6`; index avg `0.0185` n `23`; metal avg `0.12` n `18`; unknown avg `0.5756` n `669`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.5138` n `228`; crypto_major avg `-0.8084` n `8`; equity avg `0.0924` n `79`; fx avg `-0.0077` n `6`; index avg `0.0168` n `23`; metal avg `0.2215` n `18`; unknown avg `-0.3385` n `669`
- 24h: commodity avg `-0.3669` n `12`; crypto_alt avg `-0.0147` n `228`; crypto_major avg `-0.711` n `8`; equity avg `-0.4249` n `79`; fx avg `0.0286` n `6`; index avg `0.0133` n `23`; metal avg `0.4664` n `18`; unknown avg `-0.3878` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
