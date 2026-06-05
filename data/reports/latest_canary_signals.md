# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T18:52:23.911164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9374` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.554` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9288` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6532` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3767` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1732` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.8212` n `228`; crypto_major avg `-0.703` n `8`; equity avg `-0.2495` n `74`; fx avg `-0.0049` n `6`; index avg `-0.5315` n `23`; metal avg `-0.1202` n `18`; unknown avg `0.8328` n `424`
- 1h: commodity avg `0.3019` n `12`; crypto_alt avg `-2.6185` n `228`; crypto_major avg `-2.2521` n `8`; equity avg `-1.2619` n `74`; fx avg `-0.0127` n `6`; index avg `-0.8754` n `23`; metal avg `-0.5989` n `18`; unknown avg `0.2422` n `424`
- 4h: commodity avg `-0.3787` n `12`; crypto_alt avg `-3.414` n `228`; crypto_major avg `-3.3161` n `8`; equity avg `-3.562` n `74`; fx avg `-0.1007` n `6`; index avg `-2.1429` n `23`; metal avg `-1.3873` n `18`; unknown avg `-0.9375` n `424`
- 24h: commodity avg `-1.4977` n `12`; crypto_alt avg `-10.5595` n `228`; crypto_major avg `-9.0266` n `8`; equity avg `-7.3611` n `74`; fx avg `-0.069` n `6`; index avg `-4.3948` n `23`; metal avg `-4.6531` n `18`; unknown avg `-1.2683` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
