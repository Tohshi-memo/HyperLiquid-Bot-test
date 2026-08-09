# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T09:52:34.813290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.1152` n `230`; crypto_major avg `0.0601` n `8`; equity avg `0.0134` n `112`; fx avg `0.0` n `6`; index avg `-0.0014` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0202` n `785`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `0.1738` n `230`; crypto_major avg `0.1095` n `8`; equity avg `-0.0101` n `112`; fx avg `0.0007` n `6`; index avg `-0.0006` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0464` n `785`
- 4h: commodity avg `0.0562` n `12`; crypto_alt avg `0.1234` n `230`; crypto_major avg `0.1371` n `8`; equity avg `0.0008` n `112`; fx avg `-0.0121` n `6`; index avg `-0.0121` n `25`; metal avg `0.0219` n `20`; unknown avg `-0.0481` n `752`
- 24h: commodity avg `0.3146` n `12`; crypto_alt avg `1.2729` n `230`; crypto_major avg `0.3405` n `8`; equity avg `0.4841` n `112`; fx avg `-0.0245` n `6`; index avg `0.0535` n `25`; metal avg `0.0096` n `20`; unknown avg `0.313` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
