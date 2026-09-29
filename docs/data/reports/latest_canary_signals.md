# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T10:37:34.233771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0363` n `12`; crypto_alt avg `-0.1138` n `234`; crypto_major avg `-0.1255` n `8`; equity avg `0.032` n `141`; fx avg `-0.0036` n `6`; index avg `0.0076` n `26`; metal avg `0.0016` n `20`; unknown avg `0.3976` n `963`
- 1h: commodity avg `-0.0817` n `12`; crypto_alt avg `-0.0766` n `234`; crypto_major avg `-0.0966` n `8`; equity avg `0.1852` n `141`; fx avg `-0.0022` n `6`; index avg `0.041` n `26`; metal avg `0.0506` n `20`; unknown avg `202.692` n `961`
- 4h: commodity avg `-0.4613` n `12`; crypto_alt avg `1.1281` n `234`; crypto_major avg `0.3395` n `8`; equity avg `0.4497` n `141`; fx avg `-0.0441` n `6`; index avg `0.0325` n `26`; metal avg `0.018` n `20`; unknown avg `151.9386` n `945`
- 24h: commodity avg `-0.7671` n `12`; crypto_alt avg `1.2075` n `234`; crypto_major avg `0.6467` n `8`; equity avg `0.0341` n `141`; fx avg `-0.1024` n `6`; index avg `0.0116` n `26`; metal avg `-0.2085` n `20`; unknown avg `60.0644` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
