# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T06:52:28.748678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.037` n `230`; crypto_major avg `0.0274` n `8`; equity avg `0.0173` n `112`; fx avg `-0.0005` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0081` n `784`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.1087` n `230`; crypto_major avg `0.1543` n `8`; equity avg `-0.094` n `112`; fx avg `0.0014` n `6`; index avg `-0.0045` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.0028` n `752`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.3422` n `230`; crypto_major avg `0.4503` n `8`; equity avg `-0.1133` n `112`; fx avg `0.0075` n `6`; index avg `-0.0518` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.0012` n `751`
- 24h: commodity avg `-0.2511` n `12`; crypto_alt avg `-0.0586` n `230`; crypto_major avg `0.7581` n `8`; equity avg `1.2579` n `112`; fx avg `-0.0286` n `6`; index avg `0.1155` n `25`; metal avg `0.0118` n `20`; unknown avg `0.0048` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
