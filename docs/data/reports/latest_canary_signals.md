# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T09:37:16.735823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0945` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1147` n `228`; crypto_major avg `-0.0222` n `8`; equity avg `0.0636` n `67`; fx avg `0.0` n `6`; index avg `0.0188` n `23`; metal avg `0.0077` n `18`; unknown avg `-0.1887` n `396`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `0.596` n `228`; crypto_major avg `0.1689` n `8`; equity avg `0.1648` n `67`; fx avg `0.0313` n `6`; index avg `0.0044` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.0665` n `396`
- 4h: commodity avg `-0.0469` n `12`; crypto_alt avg `-1.5909` n `228`; crypto_major avg `-1.203` n `8`; equity avg `-0.1464` n `67`; fx avg `-0.0279` n `6`; index avg `-0.1085` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.1473` n `376`
- 24h: commodity avg `-0.2155` n `12`; crypto_alt avg `-5.5615` n `228`; crypto_major avg `-3.9357` n `8`; equity avg `-1.6527` n `67`; fx avg `0.0326` n `6`; index avg `-0.1317` n `23`; metal avg `-0.6854` n `18`; unknown avg `-2.1383` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
