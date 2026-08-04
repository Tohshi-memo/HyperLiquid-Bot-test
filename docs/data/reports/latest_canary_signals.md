# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T01:37:29.607025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.2552` n `230`; crypto_major avg `0.2467` n `8`; equity avg `0.1531` n `107`; fx avg `-0.004` n `6`; index avg `0.0561` n `25`; metal avg `0.0827` n `20`; unknown avg `-0.0907` n `780`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.2438` n `230`; crypto_major avg `0.3882` n `8`; equity avg `0.2403` n `107`; fx avg `-0.0344` n `6`; index avg `0.0166` n `25`; metal avg `0.0536` n `20`; unknown avg `-0.1828` n `780`
- 4h: commodity avg `0.1392` n `12`; crypto_alt avg `-0.29` n `230`; crypto_major avg `-0.2088` n `8`; equity avg `-0.2875` n `107`; fx avg `-0.0272` n `6`; index avg `-0.06` n `25`; metal avg `0.0719` n `20`; unknown avg `-0.1746` n `780`
- 24h: commodity avg `0.1276` n `12`; crypto_alt avg `0.8409` n `230`; crypto_major avg `0.66` n `8`; equity avg `1.5601` n `107`; fx avg `-0.0481` n `6`; index avg `0.1762` n `25`; metal avg `-0.0923` n `20`; unknown avg `0.1992` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
