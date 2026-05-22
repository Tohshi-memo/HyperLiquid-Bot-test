# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T18:37:18.362462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5828` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2714` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0728` n `12`; crypto_alt avg `-0.7986` n `228`; crypto_major avg `-0.7167` n `8`; equity avg `-0.1621` n `67`; fx avg `-0.0004` n `6`; index avg `-0.0505` n `23`; metal avg `-0.0757` n `18`; unknown avg `0.631` n `386`
- 1h: commodity avg `0.3548` n `12`; crypto_alt avg `-1.2865` n `228`; crypto_major avg `-0.8422` n `8`; equity avg `-0.4362` n `67`; fx avg `0.0073` n `6`; index avg `-0.1193` n `23`; metal avg `-0.0593` n `18`; unknown avg `1.0157` n `386`
- 4h: commodity avg `-0.5657` n `12`; crypto_alt avg `-1.2497` n `228`; crypto_major avg `-1.0996` n `8`; equity avg `-0.2419` n `67`; fx avg `0.0769` n `6`; index avg `0.1718` n `23`; metal avg `0.4832` n `18`; unknown avg `0.2516` n `386`
- 24h: commodity avg `-0.551` n `12`; crypto_alt avg `-1.3719` n `228`; crypto_major avg `-1.5439` n `8`; equity avg `-0.4266` n `67`; fx avg `0.1698` n `6`; index avg `0.7018` n `23`; metal avg `-0.872` n `18`; unknown avg `0.1372` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
