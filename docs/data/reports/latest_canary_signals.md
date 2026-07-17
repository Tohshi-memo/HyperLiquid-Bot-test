# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T21:52:27.365660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.1463` n `230`; crypto_major avg `-0.0425` n `8`; equity avg `-0.0427` n `96`; fx avg `-0.0001` n `6`; index avg `0.0015` n `25`; metal avg `0.0022` n `20`; unknown avg `0.0887` n `769`
- 1h: commodity avg `0.0802` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `0.0766` n `8`; equity avg `-0.0419` n `96`; fx avg `-0.0228` n `6`; index avg `0.0082` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0467` n `769`
- 4h: commodity avg `0.084` n `12`; crypto_alt avg `-0.5226` n `230`; crypto_major avg `-0.1389` n `8`; equity avg `-1.1854` n `96`; fx avg `-0.0443` n `6`; index avg `-0.1396` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.2126` n `769`
- 24h: commodity avg `0.7228` n `12`; crypto_alt avg `-1.5978` n `230`; crypto_major avg `-1.3441` n `8`; equity avg `-1.5929` n `94`; fx avg `0.0455` n `6`; index avg `-0.3234` n `25`; metal avg `-0.0481` n `20`; unknown avg `-0.054` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
