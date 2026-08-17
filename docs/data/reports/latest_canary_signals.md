# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T00:07:27.259774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0538` n `12`; crypto_alt avg `0.0434` n `230`; crypto_major avg `-0.0219` n `8`; equity avg `0.0165` n `114`; fx avg `0.0013` n `6`; index avg `-0.0018` n `25`; metal avg `0.0466` n `20`; unknown avg `-0.0222` n `792`
- 1h: commodity avg `-0.0649` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.0172` n `8`; equity avg `0.0692` n `114`; fx avg `0.0024` n `6`; index avg `0.0229` n `25`; metal avg `-0.0338` n `20`; unknown avg `0.004` n `791`
- 4h: commodity avg `-0.1852` n `12`; crypto_alt avg `-0.7458` n `230`; crypto_major avg `-0.5557` n `8`; equity avg `0.038` n `114`; fx avg `-0.0046` n `6`; index avg `0.0308` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.3985` n `791`
- 24h: commodity avg `-0.1263` n `12`; crypto_alt avg `-0.5644` n `230`; crypto_major avg `-0.327` n `8`; equity avg `0.3049` n `114`; fx avg `-0.0035` n `6`; index avg `0.0593` n `25`; metal avg `0.0583` n `20`; unknown avg `-0.0348` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
