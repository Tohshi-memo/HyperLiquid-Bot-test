# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T12:37:31.797628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.167` n `12`; crypto_alt avg `-0.3428` n `233`; crypto_major avg `-0.4881` n `8`; equity avg `-0.5103` n `134`; fx avg `-0.0047` n `6`; index avg `-0.104` n `26`; metal avg `-0.2647` n `20`; unknown avg `-0.2699` n `791`
- 1h: commodity avg `0.5301` n `12`; crypto_alt avg `-0.8908` n `233`; crypto_major avg `-0.8421` n `8`; equity avg `-1.0619` n `134`; fx avg `0.009` n `6`; index avg `-0.2076` n `26`; metal avg `-0.4837` n `20`; unknown avg `-0.1904` n `789`
- 4h: commodity avg `0.5574` n `12`; crypto_alt avg `-0.7994` n `233`; crypto_major avg `-0.9365` n `8`; equity avg `-1.3027` n `134`; fx avg `0.0294` n `6`; index avg `-0.2667` n `26`; metal avg `-0.9352` n `20`; unknown avg `0.1695` n `789`
- 24h: commodity avg `0.4607` n `12`; crypto_alt avg `-5.095` n `233`; crypto_major avg `-3.9303` n `8`; equity avg `-1.9284` n `134`; fx avg `0.1099` n `6`; index avg `-0.24` n `26`; metal avg `-0.7358` n `20`; unknown avg `-1.0539` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
