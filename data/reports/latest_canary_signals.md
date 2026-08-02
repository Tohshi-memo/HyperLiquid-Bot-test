# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T13:07:37.671065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `-0.0032` n `230`; crypto_major avg `0.0178` n `8`; equity avg `-0.0226` n `102`; fx avg `-0.0201` n `6`; index avg `0.0035` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0111` n `782`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.017` n `230`; crypto_major avg `-0.003` n `8`; equity avg `0.0671` n `102`; fx avg `-0.0047` n `6`; index avg `0.0063` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.0206` n `782`
- 4h: commodity avg `0.1715` n `12`; crypto_alt avg `-0.1408` n `230`; crypto_major avg `-0.2433` n `8`; equity avg `-0.1439` n `102`; fx avg `0.0118` n `6`; index avg `-0.0571` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0598` n `782`
- 24h: commodity avg `-1.0691` n `12`; crypto_alt avg `0.1399` n `230`; crypto_major avg `-0.007` n `8`; equity avg `0.8071` n `102`; fx avg `-0.1032` n `6`; index avg `0.1983` n `25`; metal avg `0.2397` n `20`; unknown avg `0.1964` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
