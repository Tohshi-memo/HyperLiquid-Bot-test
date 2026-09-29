# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T01:37:28.557944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3439` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0162` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0667` n `12`; crypto_alt avg `-0.7535` n `234`; crypto_major avg `-0.4652` n `8`; equity avg `0.1685` n `141`; fx avg `0.0091` n `6`; index avg `0.0298` n `26`; metal avg `-0.0089` n `20`; unknown avg `0.1396` n `963`
- 1h: commodity avg `0.1512` n `12`; crypto_alt avg `-2.1615` n `234`; crypto_major avg `-1.3839` n `8`; equity avg `-0.3767` n `141`; fx avg `0.0042` n `6`; index avg `-0.04` n `26`; metal avg `-0.0763` n `20`; unknown avg `1.7001` n `961`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `-1.2441` n `234`; crypto_major avg `-1.0624` n `8`; equity avg `-0.3095` n `141`; fx avg `-0.0045` n `6`; index avg `-0.0462` n `26`; metal avg `-0.0236` n `20`; unknown avg `0.1813` n `931`
- 24h: commodity avg `0.1909` n `12`; crypto_alt avg `-4.6891` n `234`; crypto_major avg `-2.5803` n `8`; equity avg `-2.6129` n `141`; fx avg `-0.0652` n `6`; index avg `-0.2571` n `26`; metal avg `-0.6018` n `20`; unknown avg `181.2575` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
