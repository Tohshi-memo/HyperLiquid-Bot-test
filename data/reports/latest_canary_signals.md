# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T00:52:26.454846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.0116` n `234`; crypto_major avg `-0.0091` n `8`; equity avg `0.0129` n `140`; fx avg `0.0085` n `6`; index avg `0.0011` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.108` n `943`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `0.3122` n `234`; crypto_major avg `-0.1027` n `8`; equity avg `0.0415` n `140`; fx avg `0.0136` n `6`; index avg `-0.0135` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.1314` n `935`
- 4h: commodity avg `0.1101` n `12`; crypto_alt avg `0.4044` n `234`; crypto_major avg `-0.2828` n `8`; equity avg `0.0334` n `140`; fx avg `0.0197` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.2832` n `911`
- 24h: commodity avg `-0.008` n `12`; crypto_alt avg `1.2549` n `234`; crypto_major avg `-0.4671` n `8`; equity avg `-0.0167` n `140`; fx avg `-0.066` n `6`; index avg `0.0087` n `26`; metal avg `0.0017` n `20`; unknown avg `0.1847` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
