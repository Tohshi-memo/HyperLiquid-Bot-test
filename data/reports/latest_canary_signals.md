# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T20:07:36.366041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `0.0892` n `8`; equity avg `-0.2492` n `113`; fx avg `0.0067` n `6`; index avg `0.001` n `25`; metal avg `-0.0391` n `20`; unknown avg `-0.1083` n `785`
- 1h: commodity avg `0.0494` n `12`; crypto_alt avg `0.0596` n `230`; crypto_major avg `0.3807` n `8`; equity avg `-0.4054` n `113`; fx avg `0.0207` n `6`; index avg `-0.0328` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0429` n `785`
- 4h: commodity avg `0.1876` n `12`; crypto_alt avg `-0.1342` n `230`; crypto_major avg `0.359` n `8`; equity avg `-0.656` n `113`; fx avg `0.0266` n `6`; index avg `-0.0566` n `25`; metal avg `0.1254` n `20`; unknown avg `-0.187` n `785`
- 24h: commodity avg `1.1635` n `12`; crypto_alt avg `-1.0669` n `230`; crypto_major avg `-0.8687` n `8`; equity avg `-1.794` n `113`; fx avg `0.2707` n `6`; index avg `-0.0928` n `25`; metal avg `0.149` n `20`; unknown avg `103.6002` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
