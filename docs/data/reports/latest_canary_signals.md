# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T08:15:18.565878+00:00`
- Correlation status: `ready`
- Asset price records: `343`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0954` n `7`; crypto_alt avg `0.1686` n `223`; crypto_major avg `0.0332` n `7`; equity avg `0.2367` n `47`; fx avg `0.0067` n `4`; index avg `0.1788` n `6`; metal avg `0.1191` n `7`; unknown avg `0.0077` n `312`
- 1h: commodity avg `-0.0698` n `7`; crypto_alt avg `0.47` n `223`; crypto_major avg `0.0063` n `7`; equity avg `-0.1461` n `47`; fx avg `0.0138` n `4`; index avg `0.006` n `6`; metal avg `0.0775` n `7`; unknown avg `0.3882` n `312`
- 4h: commodity avg `-0.0828` n `7`; crypto_alt avg `0.7136` n `223`; crypto_major avg `0.4137` n `7`; equity avg `0.6943` n `47`; fx avg `0.011` n `4`; index avg `0.3683` n `6`; metal avg `0.6268` n `7`; unknown avg `1.8613` n `310`
- 24h: commodity avg `0.2824` n `7`; crypto_alt avg `1.276` n `223`; crypto_major avg `0.632` n `7`; equity avg `0.0057` n `47`; fx avg `0.0006` n `4`; index avg `0.0289` n `6`; metal avg `-0.1321` n `7`; unknown avg `0.2348` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2187`, n `339`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2117`, n `339`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `339`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `339`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `339`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `339`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `339`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `339`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `335`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0952`, n `335`, weak_sample_signal
