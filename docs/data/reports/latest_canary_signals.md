# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T05:22:32.242532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0611` n `13`; crypto_alt avg `-0.0498` n `237`; crypto_major avg `0.0222` n `8`; equity avg `0.0654` n `151`; fx avg `-0.0171` n `6`; index avg `0.0321` n `26`; metal avg `0.0217` n `20`; unknown avg `0.6839` n `1200`
- 1h: commodity avg `-0.0328` n `13`; crypto_alt avg `0.0477` n `237`; crypto_major avg `0.1925` n `8`; equity avg `0.0674` n `151`; fx avg `-0.0276` n `6`; index avg `0.0322` n `26`; metal avg `-0.0152` n `20`; unknown avg `0.545` n `1198`
- 4h: commodity avg `0.0177` n `13`; crypto_alt avg `0.1803` n `237`; crypto_major avg `-0.0561` n `8`; equity avg `-0.1912` n `151`; fx avg `-0.0627` n `6`; index avg `0.0041` n `26`; metal avg `-0.0226` n `20`; unknown avg `1.0154` n `1191`
- 24h: commodity avg `0.013` n `13`; crypto_alt avg `2.4525` n `237`; crypto_major avg `1.5846` n `8`; equity avg `2.6222` n `151`; fx avg `-0.0386` n `6`; index avg `0.3882` n `26`; metal avg `-0.0898` n `20`; unknown avg `221.076` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
