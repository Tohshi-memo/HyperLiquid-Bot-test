# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T09:07:38.884015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `-0.0157` n `230`; crypto_major avg `-0.0247` n `8`; equity avg `0.0023` n `112`; fx avg `0.0088` n `6`; index avg `0.0016` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0392` n `785`
- 1h: commodity avg `0.1855` n `12`; crypto_alt avg `-0.0867` n `230`; crypto_major avg `-0.081` n `8`; equity avg `-0.109` n `112`; fx avg `0.0332` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0583` n `20`; unknown avg `-0.0167` n `785`
- 4h: commodity avg `0.1763` n `12`; crypto_alt avg `0.3202` n `230`; crypto_major avg `0.3809` n `8`; equity avg `0.2657` n `112`; fx avg `0.0978` n `6`; index avg `0.0478` n `25`; metal avg `0.0311` n `20`; unknown avg `57.1449` n `753`
- 24h: commodity avg `0.4772` n `12`; crypto_alt avg `1.0408` n `230`; crypto_major avg `0.2855` n `8`; equity avg `-0.0234` n `112`; fx avg `0.2413` n `6`; index avg `0.0887` n `25`; metal avg `-0.0934` n `20`; unknown avg `56.9648` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
