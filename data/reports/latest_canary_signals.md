# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T13:07:35.713324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1116` n `13`; crypto_alt avg `-0.0353` n `235`; crypto_major avg `-0.188` n `8`; equity avg `0.0431` n `150`; fx avg `0.0057` n `6`; index avg `0.0129` n `26`; metal avg `0.0005` n `20`; unknown avg `1.5183` n `1072`
- 1h: commodity avg `0.1001` n `13`; crypto_alt avg `-0.1005` n `235`; crypto_major avg `-0.2229` n `8`; equity avg `-0.0097` n `150`; fx avg `-0.006` n `6`; index avg `-0.0109` n `26`; metal avg `-0.1046` n `20`; unknown avg `1.0413` n `1070`
- 4h: commodity avg `-0.1455` n `13`; crypto_alt avg `0.308` n `235`; crypto_major avg `0.0429` n `8`; equity avg `0.3683` n `149`; fx avg `0.068` n `6`; index avg `0.0883` n `26`; metal avg `0.0009` n `20`; unknown avg `0.4908` n `1064`
- 24h: commodity avg `-0.5735` n `13`; crypto_alt avg `-0.3757` n `235`; crypto_major avg `-0.1155` n `8`; equity avg `0.8943` n `149`; fx avg `0.0675` n `6`; index avg `0.298` n `26`; metal avg `-0.1088` n `20`; unknown avg `0.7427` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
