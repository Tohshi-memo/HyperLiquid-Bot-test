# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T21:06:07.650908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `0.1193` n `233`; crypto_major avg `0.0418` n `8`; equity avg `0.0336` n `134`; fx avg `0.0071` n `6`; index avg `0.0049` n `26`; metal avg `0.0366` n `20`; unknown avg `1.7266` n `795`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `-0.0483` n `233`; crypto_major avg `0.0196` n `8`; equity avg `0.0971` n `134`; fx avg `-0.0072` n `6`; index avg `0.0021` n `26`; metal avg `0.0382` n `20`; unknown avg `0.7149` n `765`
- 4h: commodity avg `0.4202` n `12`; crypto_alt avg `-1.0492` n `233`; crypto_major avg `-0.5543` n `8`; equity avg `-0.6167` n `134`; fx avg `-0.0432` n `6`; index avg `-0.1091` n `26`; metal avg `-0.2837` n `20`; unknown avg `-0.196` n `765`
- 24h: commodity avg `0.0943` n `12`; crypto_alt avg `-0.4541` n `232`; crypto_major avg `-0.0553` n `8`; equity avg `0.3107` n `134`; fx avg `-0.0958` n `6`; index avg `-0.1696` n `26`; metal avg `-0.2951` n `20`; unknown avg `0.6221` n `714`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
