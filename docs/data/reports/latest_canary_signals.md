# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T16:52:16.611797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.2066` n `228`; crypto_major avg `0.0502` n `8`; equity avg `-0.0484` n `67`; fx avg `0.0006` n `6`; index avg `-0.0294` n `23`; metal avg `-0.1734` n `18`; unknown avg `-0.0044` n `386`
- 1h: commodity avg `-0.073` n `12`; crypto_alt avg `0.0739` n `228`; crypto_major avg `0.0042` n `8`; equity avg `-0.0352` n `67`; fx avg `0.0306` n `6`; index avg `0.0167` n `23`; metal avg `-0.0485` n `18`; unknown avg `-0.355` n `386`
- 4h: commodity avg `-0.3874` n `12`; crypto_alt avg `-1.3553` n `228`; crypto_major avg `-1.2197` n `8`; equity avg `-0.2639` n `67`; fx avg `0.0512` n `6`; index avg `0.319` n `23`; metal avg `-0.1302` n `18`; unknown avg `-0.637` n `386`
- 24h: commodity avg `-1.9168` n `12`; crypto_alt avg `1.1961` n `228`; crypto_major avg `0.0745` n `8`; equity avg `0.8006` n `67`; fx avg `0.1826` n `6`; index avg `1.2802` n `23`; metal avg `-0.2625` n `18`; unknown avg `-0.9773` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0405`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0395`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0384`, n `668`, weak_sample_signal
