# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T15:22:25.015109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.057` n `230`; crypto_major avg `0.147` n `8`; equity avg `0.0517` n `92`; fx avg `-0.0014` n `6`; index avg `0.0106` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0326` n `765`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.2648` n `230`; crypto_major avg `0.4225` n `8`; equity avg `0.1209` n `92`; fx avg `-0.0078` n `6`; index avg `0.0219` n `25`; metal avg `-0.0152` n `20`; unknown avg `0.1578` n `765`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `0.7692` n `230`; crypto_major avg `0.7504` n `8`; equity avg `-0.0061` n `92`; fx avg `-0.0175` n `6`; index avg `0.0179` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.1547` n `765`
- 24h: commodity avg `0.1109` n `12`; crypto_alt avg `1.1858` n `229`; crypto_major avg `0.9149` n `8`; equity avg `0.3848` n `92`; fx avg `-0.0404` n `6`; index avg `0.0894` n `25`; metal avg `0.0768` n `20`; unknown avg `3.0269` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
