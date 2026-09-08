# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T21:37:29.910399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0399` n `233`; crypto_major avg `0.0041` n `8`; equity avg `-0.0064` n `134`; fx avg `-0.005` n `6`; index avg `0.0044` n `26`; metal avg `0.0164` n `20`; unknown avg `-0.1313` n `781`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `-0.0646` n `233`; crypto_major avg `0.039` n `8`; equity avg `0.036` n `134`; fx avg `-0.0119` n `6`; index avg `-0.0006` n `26`; metal avg `0.045` n `20`; unknown avg `0.6715` n `779`
- 4h: commodity avg `0.4165` n `12`; crypto_alt avg `-0.8567` n `233`; crypto_major avg `-0.3516` n `8`; equity avg `-0.6133` n `134`; fx avg `-0.0653` n `6`; index avg `-0.1197` n `26`; metal avg `-0.2297` n `20`; unknown avg `0.6543` n `757`
- 24h: commodity avg `0.1095` n `12`; crypto_alt avg `-0.6377` n `232`; crypto_major avg `-0.0991` n `8`; equity avg `0.2647` n `134`; fx avg `-0.1125` n `6`; index avg `-0.181` n `26`; metal avg `-0.277` n `20`; unknown avg `5.5459` n `712`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
