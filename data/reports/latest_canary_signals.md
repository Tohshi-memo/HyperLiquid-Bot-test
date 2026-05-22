# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T20:22:15.331768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6852` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6272` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.2762` n `228`; crypto_major avg `-0.3186` n `8`; equity avg `-0.029` n `67`; fx avg `0.0058` n `6`; index avg `0.0309` n `23`; metal avg `0.0743` n `18`; unknown avg `-0.1065` n `386`
- 1h: commodity avg `-0.1635` n `12`; crypto_alt avg `-0.7353` n `228`; crypto_major avg `-0.6462` n `8`; equity avg `-0.1752` n `67`; fx avg `0.0101` n `6`; index avg `-0.0374` n `23`; metal avg `0.0022` n `18`; unknown avg `0.3229` n `386`
- 4h: commodity avg `-0.2312` n `12`; crypto_alt avg `-2.6421` n `228`; crypto_major avg `-1.8054` n `8`; equity avg `-0.9092` n `67`; fx avg `0.06` n `6`; index avg `-0.1202` n `23`; metal avg `-0.1782` n `18`; unknown avg `0.6947` n `386`
- 24h: commodity avg `-1.1724` n `12`; crypto_alt avg `-3.2393` n `228`; crypto_major avg `-2.5465` n `8`; equity avg `-1.0396` n `67`; fx avg `0.1905` n `6`; index avg `0.6167` n `23`; metal avg `-0.9798` n `18`; unknown avg `-1.3259` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
