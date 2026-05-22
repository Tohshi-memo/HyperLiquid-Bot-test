# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T19:22:15.953365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3839` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.121` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `0.0726` n `228`; crypto_major avg `0.0982` n `8`; equity avg `-0.1979` n `67`; fx avg `0.0008` n `6`; index avg `-0.1017` n `23`; metal avg `-0.0645` n `18`; unknown avg `0.09` n `386`
- 1h: commodity avg `0.1748` n `12`; crypto_alt avg `-1.8713` n `228`; crypto_major avg `-1.3053` n `8`; equity avg `-0.6224` n `67`; fx avg `0.0275` n `6`; index avg `-0.1843` n `23`; metal avg `-0.2883` n `18`; unknown avg `-0.2531` n `386`
- 4h: commodity avg `-0.3702` n `12`; crypto_alt avg `-1.9671` n `228`; crypto_major avg `-1.4198` n `8`; equity avg `-0.7307` n `67`; fx avg `0.0772` n `6`; index avg `-0.0359` n `23`; metal avg `-0.0924` n `18`; unknown avg `-0.6348` n `386`
- 24h: commodity avg `-0.7131` n `12`; crypto_alt avg `-2.0995` n `228`; crypto_major avg `-1.6698` n `8`; equity avg `-0.6354` n `67`; fx avg `0.175` n `6`; index avg `0.6572` n `23`; metal avg `-0.9623` n `18`; unknown avg `-0.9804` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0439`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
