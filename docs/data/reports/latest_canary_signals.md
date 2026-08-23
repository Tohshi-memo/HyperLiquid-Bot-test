# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T00:22:29.533914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.0485` n `230`; crypto_major avg `0.28` n `8`; equity avg `0.0373` n `121`; fx avg `-0.0063` n `6`; index avg `0.004` n `25`; metal avg `0.0042` n `20`; unknown avg `0.1811` n `794`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.1819` n `230`; crypto_major avg `0.6598` n `8`; equity avg `0.1025` n `121`; fx avg `0.0075` n `6`; index avg `0.0067` n `25`; metal avg `0.0008` n `20`; unknown avg `0.3049` n `794`
- 4h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.852` n `230`; crypto_major avg `-0.5216` n `8`; equity avg `0.0896` n `121`; fx avg `0.0439` n `6`; index avg `0.0148` n `25`; metal avg `0.0021` n `20`; unknown avg `0.4095` n `794`
- 24h: commodity avg `0.0786` n `12`; crypto_alt avg `-2.3179` n `230`; crypto_major avg `0.7343` n `8`; equity avg `-0.3441` n `121`; fx avg `0.1137` n `6`; index avg `-0.0574` n `25`; metal avg `-0.0609` n `20`; unknown avg `3.1083` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
