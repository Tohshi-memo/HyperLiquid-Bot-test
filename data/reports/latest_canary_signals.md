# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:52:27.930081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.066` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `0.0693` n `8`; equity avg `-0.0422` n `112`; fx avg `-0.0028` n `6`; index avg `-0.0031` n `25`; metal avg `0.0012` n `20`; unknown avg `0.1612` n `784`
- 1h: commodity avg `-0.1035` n `12`; crypto_alt avg `0.3669` n `230`; crypto_major avg `0.6578` n `8`; equity avg `0.0135` n `112`; fx avg `-0.0061` n `6`; index avg `0.0071` n `25`; metal avg `0.004` n `20`; unknown avg `0.0265` n `784`
- 4h: commodity avg `-0.0389` n `12`; crypto_alt avg `0.5096` n `230`; crypto_major avg `0.7976` n `8`; equity avg `0.174` n `112`; fx avg `0.0005` n `6`; index avg `0.0372` n `25`; metal avg `-0.0323` n `20`; unknown avg `-0.2202` n `784`
- 24h: commodity avg `-0.1784` n `12`; crypto_alt avg `1.1164` n `230`; crypto_major avg `1.1197` n `8`; equity avg `1.3051` n `112`; fx avg `-0.0159` n `6`; index avg `0.1098` n `25`; metal avg `0.0751` n `20`; unknown avg `-0.013` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
