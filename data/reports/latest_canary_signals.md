# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T04:37:32.110955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `13`; crypto_alt avg `0.019` n `235`; crypto_major avg `-0.0265` n `8`; equity avg `-0.0178` n `149`; fx avg `0.0116` n `6`; index avg `-0.0028` n `26`; metal avg `-0.018` n `20`; unknown avg `-0.1807` n `1072`
- 1h: commodity avg `-0.0178` n `13`; crypto_alt avg `0.3769` n `235`; crypto_major avg `0.226` n `8`; equity avg `0.0133` n `149`; fx avg `0.0294` n `6`; index avg `0.0022` n `26`; metal avg `-0.0241` n `20`; unknown avg `0.3032` n `1064`
- 4h: commodity avg `0.0392` n `13`; crypto_alt avg `-0.9902` n `235`; crypto_major avg `-0.4484` n `8`; equity avg `-0.196` n `149`; fx avg `0.0502` n `6`; index avg `-0.0494` n `26`; metal avg `-0.1072` n `20`; unknown avg `-0.0917` n `1064`
- 24h: commodity avg `-0.0358` n `13`; crypto_alt avg `-0.1334` n `235`; crypto_major avg `0.2144` n `8`; equity avg `0.2033` n `149`; fx avg `0.0516` n `6`; index avg `0.1335` n `26`; metal avg `0.0374` n `20`; unknown avg `585.8863` n `854`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
