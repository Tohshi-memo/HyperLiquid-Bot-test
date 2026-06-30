# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T20:07:30.071254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0645` n `228`; crypto_major avg `0.1402` n `8`; equity avg `0.066` n `88`; fx avg `0.0217` n `6`; index avg `0.0089` n `23`; metal avg `0.0061` n `20`; unknown avg `0.4895` n `765`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `-0.1126` n `228`; crypto_major avg `0.1813` n `8`; equity avg `0.2874` n `88`; fx avg `0.0187` n `6`; index avg `-0.0127` n `23`; metal avg `-0.0929` n `20`; unknown avg `1.7101` n `763`
- 4h: commodity avg `-0.1328` n `12`; crypto_alt avg `-0.0589` n `228`; crypto_major avg `0.606` n `8`; equity avg `0.521` n `88`; fx avg `0.0034` n `6`; index avg `0.0325` n `23`; metal avg `-0.0693` n `20`; unknown avg `1.3896` n `763`
- 24h: commodity avg `0.1218` n `12`; crypto_alt avg `-2.2406` n `228`; crypto_major avg `-2.1415` n `8`; equity avg `1.2724` n `88`; fx avg `0.1573` n `6`; index avg `0.2786` n `23`; metal avg `0.1767` n `20`; unknown avg `7.8615` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
