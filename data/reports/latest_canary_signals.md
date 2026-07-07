# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T02:22:25.481921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.039` n `12`; crypto_alt avg `-0.1445` n `229`; crypto_major avg `-0.1442` n `8`; equity avg `-0.0953` n `91`; fx avg `0.0101` n `6`; index avg `-0.0337` n `25`; metal avg `-0.0074` n `20`; unknown avg `1.0327` n `763`
- 1h: commodity avg `0.1389` n `12`; crypto_alt avg `-0.1574` n `229`; crypto_major avg `-0.3924` n `8`; equity avg `0.0297` n `91`; fx avg `-0.0382` n `6`; index avg `-0.0456` n `25`; metal avg `0.1933` n `20`; unknown avg `-0.1079` n `761`
- 4h: commodity avg `0.1364` n `12`; crypto_alt avg `-0.9398` n `229`; crypto_major avg `-1.0036` n `8`; equity avg `-1.2216` n `91`; fx avg `-0.0484` n `6`; index avg `-0.3783` n `25`; metal avg `-0.1997` n `20`; unknown avg `1.0945` n `761`
- 24h: commodity avg `0.2786` n `12`; crypto_alt avg `-0.0988` n `229`; crypto_major avg `-0.8376` n `8`; equity avg `-0.852` n `90`; fx avg `0.0089` n `6`; index avg `-0.1561` n `25`; metal avg `-0.3357` n `20`; unknown avg `-0.176` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
