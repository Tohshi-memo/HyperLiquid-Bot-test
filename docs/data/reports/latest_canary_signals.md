# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T06:07:32.299486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0917` n `12`; crypto_alt avg `0.1638` n `230`; crypto_major avg `0.1541` n `8`; equity avg `0.1334` n `96`; fx avg `0.0186` n `6`; index avg `0.0128` n `25`; metal avg `-0.0216` n `20`; unknown avg `0.0229` n `736`
- 1h: commodity avg `-0.2495` n `12`; crypto_alt avg `-0.6441` n `230`; crypto_major avg `-0.6684` n `8`; equity avg `-0.3113` n `96`; fx avg `0.0011` n `6`; index avg `0.0042` n `25`; metal avg `0.063` n `20`; unknown avg `-0.0896` n `736`
- 4h: commodity avg `-0.2904` n `12`; crypto_alt avg `-0.4585` n `230`; crypto_major avg `-0.8719` n `8`; equity avg `-1.2166` n `94`; fx avg `0.0074` n `6`; index avg `-0.1771` n `25`; metal avg `-0.0545` n `20`; unknown avg `-0.1209` n `736`
- 24h: commodity avg `-0.3071` n `12`; crypto_alt avg `-2.5027` n `230`; crypto_major avg `-4.0122` n `8`; equity avg `-5.8028` n `94`; fx avg `-0.1428` n `6`; index avg `-0.7479` n `25`; metal avg `-0.8761` n `20`; unknown avg `-0.6006` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
