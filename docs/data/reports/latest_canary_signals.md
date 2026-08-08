# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T15:07:31.457938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.0544` n `230`; crypto_major avg `-0.1334` n `8`; equity avg `0.0104` n `112`; fx avg `-0.0019` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0123` n `20`; unknown avg `0.0723` n `784`
- 1h: commodity avg `-0.1103` n `12`; crypto_alt avg `0.3847` n `230`; crypto_major avg `0.4994` n `8`; equity avg `-0.0229` n `112`; fx avg `-0.0024` n `6`; index avg `0.0072` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.0625` n `784`
- 4h: commodity avg `-0.0713` n `12`; crypto_alt avg `0.6188` n `230`; crypto_major avg `0.6625` n `8`; equity avg `0.1657` n `112`; fx avg `0.0021` n `6`; index avg `0.0415` n `25`; metal avg `-0.0241` n `20`; unknown avg `-0.2331` n `784`
- 24h: commodity avg `-0.2979` n `12`; crypto_alt avg `1.1234` n `230`; crypto_major avg `1.0439` n `8`; equity avg `1.0028` n `112`; fx avg `-0.0112` n `6`; index avg `0.0652` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0492` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
