# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T08:52:24.009023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0928` n `230`; crypto_major avg `-0.1271` n `8`; equity avg `-0.0638` n `114`; fx avg `-0.0165` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0735` n `20`; unknown avg `-0.0095` n `792`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.3666` n `230`; crypto_major avg `-0.3682` n `8`; equity avg `0.0406` n `114`; fx avg `-0.0279` n `6`; index avg `-0.0176` n `25`; metal avg `-0.1367` n `20`; unknown avg `0.0125` n `792`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `-0.4073` n `230`; crypto_major avg `-0.1636` n `8`; equity avg `0.5605` n `114`; fx avg `-0.0088` n `6`; index avg `0.0671` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.0584` n `776`
- 24h: commodity avg `-0.1679` n `12`; crypto_alt avg `-0.2116` n `230`; crypto_major avg `0.4116` n `8`; equity avg `1.2395` n `114`; fx avg `-0.0422` n `6`; index avg `0.1371` n `25`; metal avg `0.1357` n `20`; unknown avg `0.1297` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
