# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T19:16:07.081720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5452` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2824` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0855` n `228`; crypto_major avg `-0.0457` n `8`; equity avg `-0.1564` n `67`; fx avg `0.0018` n `6`; index avg `-0.0819` n `23`; metal avg `-0.0383` n `18`; unknown avg `-0.2015` n `386`
- 1h: commodity avg `0.1638` n `12`; crypto_alt avg `-2.0254` n `228`; crypto_major avg `-1.4468` n `8`; equity avg `-0.5813` n `67`; fx avg `0.0285` n `6`; index avg `-0.1644` n `23`; metal avg `-0.2621` n `18`; unknown avg `-0.2699` n `386`
- 4h: commodity avg `-0.3815` n `12`; crypto_alt avg `-2.1221` n `228`; crypto_major avg `-1.5612` n `8`; equity avg `-0.6895` n `67`; fx avg `0.0782` n `6`; index avg `-0.016` n `23`; metal avg `-0.0662` n `18`; unknown avg `-0.7973` n `386`
- 24h: commodity avg `-0.7243` n `12`; crypto_alt avg `-2.2535` n `228`; crypto_major avg `-1.8107` n `8`; equity avg `-0.5913` n `67`; fx avg `0.1761` n `6`; index avg `0.6775` n `23`; metal avg `-0.9364` n `18`; unknown avg `-1.2263` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
