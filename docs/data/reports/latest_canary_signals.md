# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T07:22:21.663947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2042` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0425` n `12`; crypto_alt avg `0.305` n `228`; crypto_major avg `0.1422` n `8`; equity avg `0.0824` n `72`; fx avg `0.0181` n `6`; index avg `0.005` n `23`; metal avg `-0.0398` n `18`; unknown avg `0.2356` n `420`
- 1h: commodity avg `0.1726` n `12`; crypto_alt avg `0.4263` n `228`; crypto_major avg `0.1268` n `8`; equity avg `0.0372` n `72`; fx avg `0.0043` n `6`; index avg `0.0558` n `23`; metal avg `-0.151` n `18`; unknown avg `-0.0444` n `420`
- 4h: commodity avg `0.3927` n `12`; crypto_alt avg `2.2936` n `228`; crypto_major avg `1.5676` n `8`; equity avg `0.4388` n `72`; fx avg `0.0766` n `6`; index avg `0.0045` n `23`; metal avg `-0.6366` n `18`; unknown avg `0.644` n `410`
- 24h: commodity avg `1.281` n `12`; crypto_alt avg `-1.0229` n `228`; crypto_major avg `-3.5619` n `8`; equity avg `0.9499` n `72`; fx avg `0.0599` n `6`; index avg `1.0213` n `23`; metal avg `-1.7047` n `18`; unknown avg `-0.2505` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
