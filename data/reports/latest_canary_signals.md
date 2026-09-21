# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T05:52:28.225264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0721` n `12`; crypto_alt avg `-0.1766` n `234`; crypto_major avg `-0.0648` n `8`; equity avg `0.0141` n `140`; fx avg `-0.0106` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0111` n `20`; unknown avg `2.8261` n `944`
- 1h: commodity avg `0.1063` n `12`; crypto_alt avg `-0.3637` n `234`; crypto_major avg `0.0486` n `8`; equity avg `-0.0677` n `140`; fx avg `-0.0193` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0678` n `20`; unknown avg `281.4532` n `942`
- 4h: commodity avg `0.1847` n `12`; crypto_alt avg `1.0219` n `234`; crypto_major avg `0.442` n `8`; equity avg `-0.0346` n `140`; fx avg `-0.0299` n `6`; index avg `0.0256` n `26`; metal avg `-0.1397` n `20`; unknown avg `44.8755` n `936`
- 24h: commodity avg `-0.4852` n `12`; crypto_alt avg `3.1966` n `234`; crypto_major avg `2.663` n `8`; equity avg `1.0447` n `140`; fx avg `-0.0113` n `6`; index avg `0.2216` n `26`; metal avg `-0.0218` n `20`; unknown avg `4.0689` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
