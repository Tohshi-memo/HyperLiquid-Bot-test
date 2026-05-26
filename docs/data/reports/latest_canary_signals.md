# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T21:07:18.892901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1176` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.3613` n `12`; crypto_alt avg `-0.1048` n `228`; crypto_major avg `-0.0828` n `8`; equity avg `0.0377` n `67`; fx avg `-0.0103` n `6`; index avg `-0.0006` n `23`; metal avg `0.0398` n `18`; unknown avg `0.0447` n `418`
- 1h: commodity avg `0.3104` n `12`; crypto_alt avg `-0.2005` n `228`; crypto_major avg `-0.2904` n `8`; equity avg `0.0899` n `67`; fx avg `-0.0028` n `6`; index avg `0.0157` n `23`; metal avg `0.0748` n `18`; unknown avg `-0.0716` n `418`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `-1.0404` n `228`; crypto_major avg `-0.991` n `8`; equity avg `-0.0727` n `67`; fx avg `0.0169` n `6`; index avg `0.1266` n `23`; metal avg `0.4768` n `18`; unknown avg `-0.4029` n `418`
- 24h: commodity avg `1.0469` n `12`; crypto_alt avg `-1.8983` n `228`; crypto_major avg `-1.6769` n `8`; equity avg `-0.3622` n `67`; fx avg `-0.1713` n `6`; index avg `0.3808` n `23`; metal avg `-0.8695` n `18`; unknown avg `0.1955` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
