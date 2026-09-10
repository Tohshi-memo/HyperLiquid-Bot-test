# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T04:22:27.546559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0622` n `233`; crypto_major avg `-0.0244` n `8`; equity avg `0.0161` n `134`; fx avg `0.0116` n `6`; index avg `0.0011` n `26`; metal avg `0.0016` n `20`; unknown avg `2.1936` n `797`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0186` n `233`; crypto_major avg `-0.0518` n `8`; equity avg `0.0912` n `134`; fx avg `-0.0218` n `6`; index avg `0.0192` n `26`; metal avg `0.0167` n `20`; unknown avg `0.9649` n `795`
- 4h: commodity avg `-0.0903` n `12`; crypto_alt avg `0.082` n `233`; crypto_major avg `0.3368` n `8`; equity avg `-0.2186` n `134`; fx avg `-0.0049` n `6`; index avg `-0.0063` n `26`; metal avg `0.0376` n `20`; unknown avg `8.856` n `789`
- 24h: commodity avg `0.0229` n `12`; crypto_alt avg `-3.0792` n `233`; crypto_major avg `-2.0311` n `8`; equity avg `-0.964` n `134`; fx avg `0.0473` n `6`; index avg `-0.1497` n `26`; metal avg `0.4748` n `20`; unknown avg `1.3979` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
