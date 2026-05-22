# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T16:07:25.126704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.444` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0541` n `12`; crypto_alt avg `0.0811` n `228`; crypto_major avg `-0.104` n `8`; equity avg `0.0503` n `67`; fx avg `0.008` n `6`; index avg `-0.0005` n `23`; metal avg `0.0701` n `18`; unknown avg `-0.1611` n `386`
- 1h: commodity avg `-0.3714` n `12`; crypto_alt avg `-0.0127` n `228`; crypto_major avg `-0.4251` n `8`; equity avg `0.0534` n `67`; fx avg `0.0173` n `6`; index avg `0.0635` n `23`; metal avg `0.2795` n `18`; unknown avg `-0.4395` n `386`
- 4h: commodity avg `-0.6192` n `12`; crypto_alt avg `-0.9497` n `228`; crypto_major avg `-0.9993` n `8`; equity avg `0.1029` n `67`; fx avg `0.0241` n `6`; index avg `0.4447` n `23`; metal avg `-0.3534` n `18`; unknown avg `0.1436` n `386`
- 24h: commodity avg `-1.8111` n `12`; crypto_alt avg `0.8341` n `228`; crypto_major avg `-0.5316` n `8`; equity avg `0.8054` n `67`; fx avg `0.1676` n `6`; index avg `1.1763` n `23`; metal avg `-0.3976` n `18`; unknown avg `-0.8688` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0393`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0367`, n `668`, weak_sample_signal
