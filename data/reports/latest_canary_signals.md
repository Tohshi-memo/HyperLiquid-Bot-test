# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T14:07:14.387938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.139` n `12`; crypto_alt avg `0.2313` n `228`; crypto_major avg `0.1227` n `8`; equity avg `0.0917` n `67`; fx avg `0.0044` n `6`; index avg `0.0148` n `23`; metal avg `0.0197` n `18`; unknown avg `0.0849` n `396`
- 1h: commodity avg `-0.243` n `12`; crypto_alt avg `0.3956` n `228`; crypto_major avg `0.2163` n `8`; equity avg `0.1561` n `67`; fx avg `-0.0006` n `6`; index avg `0.0832` n `23`; metal avg `0.0576` n `18`; unknown avg `0.1334` n `396`
- 4h: commodity avg `-0.1895` n `12`; crypto_alt avg `1.1613` n `228`; crypto_major avg `0.7125` n `8`; equity avg `0.3692` n `67`; fx avg `0.0075` n `6`; index avg `0.2748` n `23`; metal avg `0.0531` n `18`; unknown avg `-0.2715` n `396`
- 24h: commodity avg `-0.0439` n `12`; crypto_alt avg `-4.5639` n `228`; crypto_major avg `-3.6554` n `8`; equity avg `-1.3491` n `67`; fx avg `0.0742` n `6`; index avg `-0.1139` n `23`; metal avg `-0.1324` n `18`; unknown avg `-2.8976` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
