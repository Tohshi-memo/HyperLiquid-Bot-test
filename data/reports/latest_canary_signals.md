# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T21:28:12.656310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `0.0609` n `230`; crypto_major avg `0.0909` n `8`; equity avg `-0.0005` n `96`; fx avg `-0.0214` n `6`; index avg `0.0006` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.0572` n `769`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.0578` n `230`; crypto_major avg `0.1944` n `8`; equity avg `0.0223` n `96`; fx avg `-0.0344` n `6`; index avg `-0.001` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0499` n `769`
- 4h: commodity avg `0.0996` n `12`; crypto_alt avg `-0.3672` n `230`; crypto_major avg `0.0236` n `8`; equity avg `-1.3607` n `96`; fx avg `-0.0498` n `6`; index avg `-0.2004` n `25`; metal avg `-0.07` n `20`; unknown avg `-0.2221` n `769`
- 24h: commodity avg `0.6765` n `12`; crypto_alt avg `-1.2841` n `230`; crypto_major avg `-1.1036` n `8`; equity avg `-1.4693` n `94`; fx avg `0.0458` n `6`; index avg `-0.3152` n `25`; metal avg `-0.0263` n `20`; unknown avg `-0.0654` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
