# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T19:37:28.677866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0001` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.0475` n `230`; crypto_major avg `0.111` n `8`; equity avg `-0.0484` n `94`; fx avg `-0.0019` n `6`; index avg `-0.0204` n `25`; metal avg `-0.0733` n `20`; unknown avg `0.118` n `768`
- 1h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.0067` n `230`; crypto_major avg `0.1973` n `8`; equity avg `-0.2859` n `94`; fx avg `0.0111` n `6`; index avg `-0.0902` n `25`; metal avg `-0.0176` n `20`; unknown avg `-0.0253` n `768`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `-0.8307` n `230`; crypto_major avg `-1.2947` n `8`; equity avg `-1.162` n `94`; fx avg `-0.0271` n `6`; index avg `-0.2946` n `25`; metal avg `-0.4388` n `20`; unknown avg `-0.1808` n `768`
- 24h: commodity avg `-0.3886` n `12`; crypto_alt avg `-0.8689` n `230`; crypto_major avg `-1.854` n `8`; equity avg `-3.7667` n `94`; fx avg `-0.1514` n `6`; index avg `-0.5625` n `25`; metal avg `-0.8393` n `20`; unknown avg `-0.401` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
