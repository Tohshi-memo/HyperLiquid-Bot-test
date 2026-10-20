# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T05:22:29.968076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.0549` n `237`; crypto_major avg `-0.0421` n `8`; equity avg `-0.0469` n `151`; fx avg `0.0112` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0393` n `20`; unknown avg `-0.1318` n `1198`
- 1h: commodity avg `0.0117` n `13`; crypto_alt avg `-0.4946` n `237`; crypto_major avg `-0.2404` n `8`; equity avg `-0.393` n `151`; fx avg `0.0092` n `6`; index avg `-0.0717` n `26`; metal avg `-0.0795` n `20`; unknown avg `-0.3391` n `1194`
- 4h: commodity avg `-0.027` n `13`; crypto_alt avg `0.8441` n `237`; crypto_major avg `0.648` n `8`; equity avg `-0.0689` n `151`; fx avg `0.0254` n `6`; index avg `-0.0197` n `26`; metal avg `0.2081` n `20`; unknown avg `1.9386` n `1188`
- 24h: commodity avg `0.2584` n `13`; crypto_alt avg `0.394` n `237`; crypto_major avg `-0.3136` n `8`; equity avg `-1.3783` n `151`; fx avg `0.0133` n `6`; index avg `-0.253` n `26`; metal avg `-0.2434` n `20`; unknown avg `5.4238` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
