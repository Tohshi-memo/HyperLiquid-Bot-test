# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T09:22:25.685796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.1147` n `228`; crypto_major avg `-0.0348` n `8`; equity avg `0.001` n `88`; fx avg `-0.0006` n `6`; index avg `0.003` n `23`; metal avg `0.0017` n `20`; unknown avg `0.0263` n `764`
- 1h: commodity avg `-0.0754` n `12`; crypto_alt avg `0.3684` n `228`; crypto_major avg `0.399` n `8`; equity avg `0.1334` n `88`; fx avg `0.0173` n `6`; index avg `0.0225` n `23`; metal avg `0.0139` n `20`; unknown avg `-0.115` n `764`
- 4h: commodity avg `-0.0392` n `12`; crypto_alt avg `0.522` n `228`; crypto_major avg `0.7583` n `8`; equity avg `0.3134` n `88`; fx avg `0.0198` n `6`; index avg `0.0669` n `23`; metal avg `0.0199` n `20`; unknown avg `-0.1789` n `724`
- 24h: commodity avg `0.1526` n `12`; crypto_alt avg `0.389` n `228`; crypto_major avg `-0.3385` n `8`; equity avg `0.1443` n `88`; fx avg `0.034` n `6`; index avg `-0.0604` n `23`; metal avg `-0.0187` n `20`; unknown avg `16.3326` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2186`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
